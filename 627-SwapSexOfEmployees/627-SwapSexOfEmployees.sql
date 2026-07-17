-- Last updated: 7/17/2026, 3:06:15 PM
UPDATE salary SET sex =
CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;