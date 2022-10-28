import parse_library_results_maven # Code to test
import unittest # Test framework

class Test_ParseLibraryPostText(unittest.TestCase):
    
    """ Description	"""
    def test_get_site_content():
    
        """ Description
        :raises:
    
        :rtype:
        """    
        #Arrange
        try:
            url = "url"
        
        except:
            print("No URL found.")

        #Act and assert
        assert(parse_library_results_maven.get_site_content(url), True)

    def test_get_artifact_page():
    
        """ Description
        :raises:
    
        :rtype:
        """    
        #Arrange
        try:
            library_name = "library name"
            response = "response"
        
        except:
            print("No library name found.")

        #Act and assert
        assert(parse_library_results_maven.get_artifact_page(response.text, library_name), True)
    
    def test_get_version_rows():
    
        """ Description
        :raises:
    
        :rtype:
        """    
        #Arrange
        try:
            tables = "table"
        
        except:
            print("No table found")

        #Act and assert
        assert(parse_library_results_maven.get_version_rows(tables), True)
    
    def test_get_library_version_rows():
        #Arrange
        try:
            tables = "table"
        
        except:
            print("No library table found")

        #Act and assert
        assert(parse_library_results_maven.get_library_version_rows(tables), True)

    def test_parse_library_details_page():
        #Arrange
        try:
            tables = "table"
            response = "response"
        
        except:
            print("No tables or response.")
        
        #Act and assert
        assert(parse_library_results_maven.get_parse_library_details_page(response.text, tables), True)