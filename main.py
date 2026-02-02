import astropy.units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
from astropy.coordinates import get_sun

# 1. Setup Location and Time
# Using Roseville, California (approximate for your current location)
location = EarthLocation(lat=38.7521*u.deg, lon=-121.2858*u.deg, height=50*u.m)

# Current Time
now = Time.now()

# 2. Define M31 and get Equatorial Coordinates
m31 = SkyCoord.from_name("M31")
ra_dec_now = m31.transform_to('icrs')

print(f"--- M31 Current Coordinates (Time: {now}) ---")
#print(f"RA:  {ra_dec_now.ra}")
#print(f"Dec: {ra_dec_now.dec}")

# 3. Calculate Horizontal Coordinates (Alt/Az)
altaz_frame = AltAz(obstime=now, location=location)
m31_altaz = m31.transform_to(altaz_frame)

#print(f"Alt: {m31_altaz.alt:.4f}")
#print(f"Az:  {m31_altaz.az:.4f}\n")
ra_hms = ra_dec_now.ra.to_string(unit=u.hour, sep='hms', precision=1)
dec_dms = ra_dec_now.dec.to_string(unit=u.degree, sep='dms', precision=0, alwayssign=True)
print(f"{ra_hms} {dec_dms}")


# --- SECOND PART: Manual Timestamp Conversion ---

# 4. Use specific time: Jan 12, 2012, at 19:00:00
specific_time = Time("2012-01-12 19:00:00")
specific_frame = AltAz(obstime=specific_time, location=location)

# Calculate Alt/Az for that specific historical moment
m31_historical = m31.transform_to(specific_frame)
alt_val = m31_historical.alt
az_val = m31_historical.az

# 5. Convert that Alt/Az back into RA/Dec
# This demonstrates that RA/Dec are fixed relative to the stars,
# while Alt/Az change based on time/location.
reconstructed_coord = SkyCoord(alt=alt_val, az=az_val, frame=specific_frame)
final_ra_dec = reconstructed_coord.transform_to('icrs')

print(f"--- Reconstruction from {specific_time} ---")
print(f"Input Alt/Az: {alt_val:.2f}, {az_val:.2f}")
#print(f"Generated RA:  {final_ra_dec.ra}")
#print(f"Generated Dec: {final_ra_dec.dec}")
ra_hms = final_ra_dec.ra.to_string(unit=u.hour, sep='hms', precision=1)
dec_dms = final_ra_dec.dec.to_string(unit=u.degree, sep='dms', precision=0, alwayssign=True)
print(f"{ra_hms} {dec_dms}")
print("di,,,ummy")
Print("a second commit")

