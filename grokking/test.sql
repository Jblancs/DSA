drop view “RestaurantSearchViewNew”;
create view
  “RestaurantSearchViewNew” as
select
  r.restaurant_id,
  r.name as restaurant_name,
  r.website as restaurant_website,
  c.name as company_name,
  c.company_id as company_id,
  a.latitude,
  a.longitude,
  a.location,
  a.street_1,
  a.street_2,
  a.city,
  a.state,
  a.zip_code,
  a.country,
  array_agg(distinct case when rc.type=‘SECONDARY’ and ct.internal_name is not null then ct.internal_name end) as cuisines,
  array_agg(distinct case when rc.type = ‘PRIMARY’ and ct.internal_name is not null then ct.name end) as primary_cuisines,
  array_agg(distinct case when rc.type = ‘PRIMARY’ and ct.cuisine_id is not null then ct.cuisine_id end) as primary_cuisine_ids,
  array_agg(distinct l.name) filter (where mi.item_type IN (‘PRIMARY’, ‘SIDE’)) as labels,
  array_agg(distinct mil.verification_type) filter (where mil.verification_type is not null) as verification_types,
  array_agg(distinct e.email_address) filter (where e.email_address is not null) as emails,  -- Filtering out null email addresses
  array_agg(distinct p.phone_number) filter (where p.phone_number is not null) as phone_numbers,  -- Filtering out null phone numbers
  (select bp.photo_urls from “BusinessPhotos” bp
  where bp.company_id = c.company_id and bp.image_type = ‘LOGO’ limit 1) as company_logo,  -- Aggregating the logo URL
  jsonb_agg(DISTINCT bp.photo_urls) filter (where bp.image_type = ‘MAIN’) as company_photos
from
  “Restaurant” r
  join “RestaurantLocations” rl on r.restaurant_id = rl.restaurant_id
  join “Addresses” a on rl.address_id = a.address_id
  left join “RestaurantCuisines” rc on r.restaurant_id = rc.restaurant_id
  left join “CuisineTypes” ct on rc.cuisine_id = ct.cuisine_id
  -- Join the Menus table twice: once for the direct restaurant-menu relationship and once for the company-restaurant-menu relationship
  left join “Companies” c on r.company_id = c.company_id
  left join “Menus” m on (r.restaurant_id = m.restaurant_id OR c.company_id = m.company_id)
  left join “MenuItemMenus” mim on m.id = mim.menu_id
  left join “MenuItems” mi on mim.menu_item_id = mi.menu_item_id
  left join “MenuItemLabels” mil on mim.menu_item_id = mil.menu_item_id
  left join “Labels” l on mil.label_id = l.id
  -- Join the ContactInfo, EmailAddresses, and PhoneNumbers
  left join “ContactInfo” ci on r.contact_id = ci.contact_id
  left join “EmailAddresses” e on ci.contact_id = e.contact_id
  left join “PhoneNumbers” p on ci.contact_id = p.contact_id
  left join “BusinessPhotos” bp on c.company_id = bp.company_id
group by
  r.restaurant_id,
  r.name,
  r.website,
  c.name,
  c.company_id,
  a.latitude,
  a.longitude,
  a.location,
  a.street_1,
  a.street_2,
  a.city,
  a.state,
  a.zip_code,
  a.country;

--   ------------------------------------------------------------------------------------------------
-- Supabase AI is experimental and may produce incorrect answers
-- Always verify the output before executing
-- DROP FUNCTION IF EXISTS find_nearby_restaurants_by_distance_or_cuisines_with_pagination(double precision, double precision, text[], double precision, int, int);
drop function find_nearby_restaurants_by_distance_or_cuisines_with_pagination (float, float, varchar, float, int, int, text[]);
create
or replace function find_nearby_restaurants_by_distance_or_cuisines_with_pagination (
  lat float,
  long float,
  cuisineType varchar default null,
  max_distance_miles float default null,
  offset_val int default 0,
  limit_val int default 20,
  dietary_preferences text[] default null
) returns table (
  restaurant_id uuid,
  name text,
  restaurant_website text,
  latitude float,
  longitude float,
  location geography,
  -- cuisines text[],
  -- primary_cuisines text[],
  -- labels text[],
  street_1 varchar,
  street_2 varchar,
  city varchar,
  state varchar,
  zip_code varchar,
  country varchar,
  -- emails text[],
  -- phone_numbers varchar[],
  -- verification_types varchar[],
  -- company_logo jsonb,
  -- company_photos jsonb,
  dist_miles float
) language sql as $$
  WITH ranked_restaurants AS (
    SELECT
      restaurant_id,
      restaurant_name,
      restaurant_website,
      ST_Y(location::geometry) as latitude,
      ST_X(location::geometry) as longitude,
      location,
      cuisines,
      primary_cuisines,
      labels,
      street_1,
      street_2,
      city,
      state,
      zip_code,
      country,
      emails,
      phone_numbers,
      verification_types,
      company_logo,
      company_photos,
      ST_Distance(location, ST_Point(long, lat)::geography) / 1609.34 AS dist_miles
    from “RestaurantSearchViewNew”
    where (cuisineType is null or cuisines @> array[cuisineType])
      AND (
        dietary_preferences is null
        OR (
          ARRAY(SELECT LOWER(unnest(labels))) @> ARRAY(SELECT LOWER(unnest(dietary_preferences::text[])))
        )
      )
    order by location <-> st_point(long, lat):: geography
  )
  SELECT *
  FROM ranked_restaurants
  WHERE (max_distance_miles IS NULL OR dist_miles <= max_distance_miles)
  OFFSET offset_val
  LIMIT limit_val;
$$;

--   ------------------------------------------------------------------------------------------------

DROP FUNCTION IF EXISTS find_nearby_restaurants_by_distance_or_cuisines(
    double precision,
    double precision,
    character varying,
    double precision,
    character varying
);
create or replace function find_nearby_restaurants_by_distance_or_cuisines(
  lat float,
  long float,
  cuisineType varchar default null,
  max_distance_miles float default null,
  search_query varchar DEFAULT NULL
) returns table (
  restaurant_id uuid,
  name text,
  restaurant_website text,
  latitude float,
  longitude float,
  location geography,
  cuisines text[],
  primary_cuisines text[],
  labels text[],
  street_1 varchar,
  street_2 varchar,
  city varchar,
  state varchar,
  zip_code varchar,
  country varchar,
  emails text[],
  phone_numbers varchar[],
  verification_types varchar[],
  company_logo jsonb,
  company_photos jsonb,
  dist_miles float
) language sql as $$
  with ranked_restaurants as (
    select
      restaurant_id,
      restaurant_name,
      restaurant_website,
      st_y(location::geometry) as latitude,
      st_x(location::geometry) as longitude,
      location,
      cuisines,
      primary_cuisines,
      labels,
      street_1,
      street_2,
      city,
      state,
      zip_code,
      country,
      emails,
      phone_numbers,
      verification_types,
      company_logo,
      company_photos,
      st_distance(location, st_point(long, lat)::geography) / 1609.34 as dist_miles
    from “RestaurantSearchViewNew”
    WHERE ST_DWithin(
      location,
      ST_SetSRID(ST_MakePoint(long, lat), 4326)::geography,
      max_distance_miles * 1609.34
    ) and ((cuisineType is null or cuisines @> array[cuisineType])) and ((search_query IS NULL OR restaurant_name ILIKE ‘%’ || search_query || ‘%’))
    order by location <-> st_point(long, lat):: geography
  )
  select * from ranked_restaurants where (max_distance_miles is null or dist_miles <= max_distance_miles);
$$;
--   ------------------------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION find_nearby_restaurants_by_distance_or_cuisines(
  lat numeric,
  long numeric,
  cuisineType varchar DEFAULT NULL,
  max_distance_miles float DEFAULT NULL,
  search_query varchar DEFAULT NULL
) RETURNS TABLE (
  restaurant_id uuid,
  name varchar,
  website varchar,
  company_id uuid,
  latitude numeric,
  longitude numeric,
  location geography,
  street_1 varchar,
  street_2 varchar,
  city varchar,
  state varchar,
  zip_code varchar,
  country varchar,
  cuisines varchar[],
  primary_cuisines varchar[],
  labels text[],
  verification_types varchar[],
  company_logo JSONB,
  company_photos JSONB
  -- dist_miles float
) LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY WITH RestaurantBase AS (
    SELECT
      fl.restaurant_id,
      fl.name,
      fl.website,
      fl.company_id,
      fl.latitude,
      fl.longitude,
      fl.location,
      fl.street_1,
      fl.street_2,
      fl.city,
      fl.state,
      fl.zip_code,
      fl.country
      -- fl.dist_miles
      -- ST_Distance(fl.location, ST_SetSRID(ST_MakePoint(long, lat), 4326)::geography) / 1609.34 AS dist_miles
    FROM get_filtered_restaurant_locations(lat, long, max_distance_miles) AS fl
    WHERE (search_query IS NULL OR fl.name ILIKE ‘%’ || search_query || ‘%’)
  ), CuisineInfo AS (
    SELECT
      rc.restaurant_id,
      array_agg(DISTINCT ct.internal_name) FILTER (WHERE rc.type = ‘SECONDARY’) AS cuisines,
      array_agg(DISTINCT ct.internal_name) FILTER (WHERE rc.type = ‘PRIMARY’) AS primary_cuisines,
      array_agg(DISTINCT ct.cuisine_id) FILTER (WHERE rc.type = ‘PRIMARY’) AS primary_cuisine_ids
    FROM “RestaurantCuisines” rc
    JOIN “CuisineTypes” ct ON rc.cuisine_id = ct.cuisine_id
    GROUP BY rc.restaurant_id
  ), LabelAndVerification AS (
    SELECT
      m.restaurant_id,
      array_agg(DISTINCT l.name) FILTER (WHERE mi.item_type IN (‘PRIMARY’, ‘SIDE’)) AS labels,
      array_agg(DISTINCT mil.verification_type) FILTER (WHERE mil.verification_type IS NOT NULL) AS verification_types
    FROM “Menus” m
    JOIN “MenuItemMenus” mim ON m.id = mim.menu_id
    JOIN “MenuItems” mi ON mim.menu_item_id = mi.menu_item_id
    LEFT JOIN “MenuItemLabels” mil ON mi.menu_item_id = mil.menu_item_id
    LEFT JOIN “Labels” l ON mil.label_id = l.id
    GROUP BY m.restaurant_id
  ), PhotoInfo AS (
    SELECT
      c.company_id,
      (SELECT bp.photo_urls FROM “BusinessPhotos” bp WHERE bp.company_id = c.company_id AND bp.image_type = ‘LOGO’ LIMIT 1) AS company_logo,
      jsonb_agg(DISTINCT bp.photo_urls) FILTER (WHERE bp.image_type = ‘MAIN’) AS company_photos
    FROM “Companies” c
    JOIN “BusinessPhotos” bp ON c.company_id = bp.company_id
    GROUP BY c.company_id
  )
  SELECT
    rb.restaurant_id,
    rb.name,
    rb.website,
    rb.company_id,
    rb.latitude,
    rb.longitude,
    rb.location,
    rb.street_1,
    rb.street_2,
    rb.city,
    rb.state,
    rb.zip_code,
    rb.country,
    -- rb.dist_miles,
    ci.cuisines,
    ci.primary_cuisines,
    lav.labels,
    lav.verification_types,
    pi.company_logo,
    pi.company_photos
  FROM RestaurantBase rb
  LEFT JOIN CuisineInfo ci ON rb.restaurant_id = ci.restaurant_id
  LEFT JOIN LabelAndVerification lav ON rb.restaurant_id = lav.restaurant_id
  LEFT JOIN PhotoInfo pi ON rb.restaurant_id = pi.company_id  -- Adjusted join condition to match restaurant_id with company_id
  -- ORDER BY rb.dist_miles
  order by rb.location <-> st_point(long, lat):: geography
  LIMIT 50;
END;
$$;
--   -----------------------------------------------------------
CREATE OR REPLACE FUNCTION get_filtered_restaurant_locations(
    lat numeric,
    long numeric,
    max_distance_miles FLOAT DEFAULT 50
)
RETURNS TABLE (
    restaurant_id UUID,
    name varchar,
    website varchar,
    company_id UUID,
    latitude numeric,
    longitude numeric,
    location GEOGRAPHY,
    street_1 varchar,
    street_2 varchar,
    city varchar,
    state varchar,
    zip_code varchar,
    country varchar
    -- dist_miles float
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        r.restaurant_id,
        r.name,
        r.website,
        r.company_id,
        a.latitude,
        a.longitude,
        a.location,
        a.street_1,
        a.street_2,
        a.city,
        a.state,
        a.zip_code,
        a.country
        -- ST_SetSRID(ST_MakePoint(long, lat), 4326)::geography,
        --     max_distance_miles * 1609.34
    FROM
        “Restaurant” r
    JOIN
        “RestaurantLocations” rl ON r.restaurant_id = rl.restaurant_id
    JOIN
        “Addresses” a ON rl.address_id = a.address_id
    WHERE
        ST_DWithin(
            a.location,
            ST_SetSRID(ST_MakePoint(long, lat), 4326)::geography,
            max_distance_miles * 1609.34
        );
END;
$$ LANGUAGE plpgsql;
