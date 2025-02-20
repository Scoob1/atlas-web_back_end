-- Lists all bands with Glam rock as their main style rank by longevity
SELECT band_name AS 'band_name',
        TIMESTAMPDIFF(YEAR, formed, IFNULL(split, 2024)) AS lifespan
FROM metal_bands
WHERE LOWER(style) = '%Glam rock%'
ORDER BY lifespan DESC;
