import unittest, math, sun_position

DAY = 328
GEOGRAPHICAL_LONGITUDE = math.radians(5)
GEOGRAPHICAL_LATITUDE = math.radians(52)
LOCAL_CLOCK_TIME = 15.0

class TestExample(unittest.TestCase):
    """ Tests the example provided in Calculation_Sunposition.pdf """
    
    def test_rad_day(self):
        """ Calculation_Sunposition.pdf example: get_rad_day """
        self.assertAlmostEqual(round(math.degrees(sun_position.get_rad_day(DAY)), 4), 323.5068)
    
    def test_equation_of_time(self):
        """ Calculation_Sunposition.pdf example: get_equation_of_time """
        self.assertAlmostEqual(round(sun_position.get_equation_of_time(DAY), 4), 0.2196)
            
    def test_true_solar_time(self):
        """ Calculation_Sunposition.pdf example: get_true_solar_time """
        self.assertAlmostEqual(round(sun_position.get_true_solar_time(LOCAL_CLOCK_TIME, GEOGRAPHICAL_LONGITUDE, 0.2196), 4), 14.5529)
        
    def test_hour_angle(self):
        """ Calculation_Sunposition.pdf example: get_hour_angle """
        # Removed one digit due to the limited input
        self.assertAlmostEqual(round(math.degrees(sun_position.get_hour_angle(14.5529)), 3), 38.293)
        
    def test_sun_declination(self):
            """ Calculation_Sunposition.pdf example: get_sun_declination """
            self.assertAlmostEqual(round(math.degrees(sun_position.get_sun_declination(DAY)), 4), -20.4227)
        
    def test_sun_elevation_angle(self):
        """ Calculation_Sunposition.pdf example: get_sun_elevation_angle """
        self.assertAlmostEqual(round(math.degrees(sun_position.get_sun_elevation_angle(GEOGRAPHICAL_LATITUDE, math.radians(-20.4227), math.radians(38.2939))), 4), 10.2448)
        
    def test_sun_azimuth_angle(self):
        """ Calculation_Sunposition.pdf example: get_sun_azimuth_angle """
        self.assertAlmostEqual(round(math.degrees(sun_position.get_sun_azimuth_angle(math.radians(10.2448), GEOGRAPHICAL_LATITUDE, math.radians(-20.4227), 14.5529)), 4), 216.1678)
    
    def test_time_sunset(self):
        """ Calculation_Sunposition.pdf example: get_time_sunset """
        self.assertAlmostEqual(round(sun_position.get_time_sunset(GEOGRAPHICAL_LATITUDE, math.radians(-20.4227)), 4), 16.1025)