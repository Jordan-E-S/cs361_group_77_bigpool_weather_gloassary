from fastapi import FastAPI

app = FastAPI()

# Dictionary of weather terms source from https://www.weather.gov/otx/Full_Weather_Glossary
weather_terms = {

"ACID RAIN": "Cloud or rain droplets containing pollutants such as oxides of sulfur and nitrogen, making them acidic.",
"ADIABATIC": "Changes in temperature caused by expansion or compression of air as it rises or descends.",
"ADVECTION": "The horizontal transport of air or atmospheric properties such as heat or moisture.",
"ADVISORY": "Issued for weather situations that cause significant inconvenience but are not severe enough for warnings.",
"AGL": "Above Ground Level.",
"AIR MASS": "A large body of air with similar temperature and moisture characteristics.",
"ALBEDO": "The percentage of light reflected by an object.",
"ANEMOMETER": "An instrument used to measure wind speed.",
"ANTICYCLONE": "A large area of high pressure with clockwise winds in the Northern Hemisphere.",
"ARCTIC AIR": "A mass of very cold, dry air originating over the Arctic region.",

"BACKING WINDS": "A counterclockwise change in wind direction.",
"BAROMETER": "An instrument used to measure atmospheric pressure.",
"BEAUFORT SCALE": "A scale indicating wind speed based on observed effects.",
"BLACK ICE": "Thin transparent ice commonly forming on roadways.",
"BLIZZARD": "A storm with strong winds and blowing snow reducing visibility.",
"BLOWING SNOW": "Wind-driven snow that reduces surface visibility.",
"BOW ECHO": "A radar pattern associated with strong thunderstorm winds.",
"BREEZY": "Sustained winds of approximately 15 to 25 mph.",

"CAA": "Cold Air Advection.",
"CALM": "Absence of noticeable air movement.",
"CEILING": "Height of the lowest cloud layer when skies are broken or overcast.",
"CELSIUS": "Temperature scale where water freezes at 0° and boils at 100°.",
"CHINOOK": "A warm dry wind descending along mountain slopes.",
"CIRRUS": "High altitude clouds composed of ice crystals.",
"CLIMATE": "Long-term average weather conditions.",
"CLOUDY": "Sky covered by clouds for 90% or more.",
"COLD FRONT": "Boundary where cold air advances into warmer air.",
"CONDENSATION": "Process where water vapor turns into liquid water.",

"DEW": "Moisture condensed on surfaces when temperatures fall.",
"DEWPOINT": "Temperature at which air becomes saturated with moisture.",
"DENSE FOG": "Fog reducing visibility to one quarter mile or less.",
"DIVERGENCE": "Spreading apart of winds in the atmosphere.",
"DOPPLER RADAR": "Radar used to measure velocity of precipitation particles.",
"DRIZZLE": "Light precipitation consisting of fine droplets.",
"DUST STORM": "Strong winds lifting dust reducing visibility.",

"EL NIÑO": "Warming of Pacific Ocean waters affecting global weather.",
"ENSO": "El Niño–Southern Oscillation climate pattern.",
"EVAPORATION": "Process where liquid water turns into vapor.",

"FAHRENHEIT": "Temperature scale used primarily in the United States.",
"FLASH FLOOD": "Rapid flooding caused by intense rainfall.",
"FOG": "Cloud at ground level reducing visibility.",
"FREEZE": "Temperature falling to or below 32°F.",
"FROST": "Ice crystals forming on surfaces under freezing conditions.",
"FUNNEL CLOUD": "Rotating column of air extending from a cloud but not reaching the ground.",

"GALE": "Strong winds ranging from 39 to 54 mph.",
"GEOSTATIONARY SATELLITE": "Satellite that remains above the same Earth location.",
"GREENHOUSE EFFECT": "Warming caused by gases trapping heat in the atmosphere.",
"GUST": "Sudden increase in wind speed.",
"GUST FRONT": "Leading edge of cool air flowing out from a thunderstorm.",

"HAIL": "Frozen precipitation falling in lumps or balls.",
"HEAT INDEX": "Perceived temperature due to heat and humidity.",
"HUMIDITY": "Amount of water vapor present in the air.",
"HURRICANE": "Severe tropical cyclone with winds exceeding 74 mph.",

"INVERSION": "Increase in temperature with height in the atmosphere.",
"ISOBAR": "Line of equal atmospheric pressure on a weather map.",
"ISOTHERM": "Line connecting points of equal temperature.",

"JET STREAM": "Fast flowing air current high in the atmosphere.",

"KATABATIC WIND": "Wind flowing downhill due to gravity.",
"KNOT": "Unit of speed equal to one nautical mile per hour.",

"LA NIÑA": "Cooling of Pacific Ocean waters affecting global weather.",
"LAPSE RATE": "Rate at which temperature decreases with altitude.",
"LIGHTNING": "Electrical discharge during thunderstorms.",
"LOW": "Area of low atmospheric pressure.",

"MACROBURST": "Large downdraft producing damaging winds.",
"MARITIME AIR MASS": "Moist air mass formed over oceans.",
"METEOROLOGY": "Study of the atmosphere and weather.",
"MICROBURST": "Localized downdraft producing intense winds.",

"NEXRAD": "Network of Doppler radars across the United States.",
"NOAA": "National Oceanic and Atmospheric Administration.",

"OCCLUDED FRONT": "Front formed when a cold front overtakes a warm front.",
"OVERCAST": "Sky covered by clouds more than 90%.",

"PRECIPITATION": "Water falling from the atmosphere as rain, snow, etc.",
"PRESSURE": "Force exerted by the atmosphere.",

"RADAR": "System detecting precipitation using radio waves.",
"RAIN": "Liquid precipitation falling from clouds.",
"RELATIVE HUMIDITY": "Percentage of moisture in the air compared to maximum possible.",
"RIDGE": "Elongated region of high pressure.",

"SEA BREEZE": "Wind blowing from sea toward land.",
"SLEET": "Ice pellets formed from freezing raindrops.",
"SNOW": "Frozen precipitation falling as flakes.",
"SUPERCELL": "Highly organized rotating thunderstorm.",

"TEMPERATURE": "Measure of heat or cold.",
"THUNDER": "Sound produced by lightning heating the air.",
"THUNDERSTORM": "Storm producing lightning and thunder.",
"TORNADO": "Violently rotating column of air touching the ground.",
"TROUGH": "Elongated region of low pressure.",

"UNSTABLE AIR": "Air that rises easily and can produce storms.",

"VEERING WINDS": "Clockwise change in wind direction.",

"WARM FRONT": "Boundary where warm air replaces cooler air.",
"WARNING": "Issued when dangerous weather is occurring or imminent.",
"WATCH": "Indicates conditions favorable for hazardous weather.",
"WIND": "Movement of air relative to Earth’s surface.",
"WIND CHILL": "Perceived decrease in air temperature due to wind.",
"WIND SHEAR": "Change in wind speed or direction with height.",

"X-BAND": "Microwave frequency band used by some radars.",

"ZONAL WIND": "Wind blowing parallel to latitude lines."
}


@app.get("/")
def read_root():
    return {"message": "Weather Terms Microservice Running"}


# Return terms starting with a letter
@app.get("/terms/")
def get_terms(letter: str):
    letter = letter.upper()

    results = [term for term in weather_terms if term.startswith(letter)]

    return {
        "letter": letter,
        "terms": sorted(results)
    }


# Return definition of a term
@app.get("/definition/")
def get_definition(term: str):

    key = term.upper()

    if key not in weather_terms:
        return {"error": "Term not found"}

    return {
        "term": key,
        "definition": weather_terms[key]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
