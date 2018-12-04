from mathematicians_rank import simple_get
import unittest

class TestSimpleGet(unittest.TestCase):

    def test_sample_html_content_is_returned(self):
        # Test the results of the function against the sample HTML file in the root
        pass

    def test_sample_xml_content_is_returned(self):
        # Test the results of the function against the sample XML file in the root
        pass

    def test_file_that_is_not_html_or_xml_returns_None(self):
        # Test the reusults of the function against a sample JSON file
        pass

    def test_that_an_error_is_printed_if_function_fails(self):
        # Test that the error catching we have in place will actually output an error
        pass

class TestGetNames(unittest.TestCase):

    def test_that_an_error_is_printed_if_no_content_is_pulled(self):
        # Test that an error is printed to the console if there is no content pulled
        pass

    def test_that_only_a_string_can_be_a_valid_url(self):
        # Test that any other type of string or int will cause the function to fail
        pass

    def test_that_the_function_returns_a_list(self):
        # Ensure that a set is returned
        pass

    def test_ensure_there_are_no_duplicates_in_list(self):
        # Ensure the same item does not appear twice within the returned list
        pass

    def test_that_an_empty_li_does_not_end_up_in_returned_list(self):
        # What if a li is empty, will a empty string be returned?
        pass

class TestGetHitsOnNames(unittest.TestCase):

    def test_if_names_are_list_or_set_that_first_item_is_searched(self):
        # I've already had the experience of adding a list instead of a string (the difference between names[1] and
        # names[:1] is intense)
        pass

    def test_an_error_is_returned_if_names_can_not_be_converted_to_string(self):
        # If names are an int or something, it should say that this format is not accepted
        pass

    def test_all_spaces_are_converted_to_uri_readable_format(self):
        # Ensure that all the spaces within the names are converted to %20 so they can be read by thr browser more easily
        pass

    def test_ascii_characters_within_namesare_accepted_or_converted(self):
        # Some names, such as Poincaré have ascii characters in them - currently these are returning invalid responses
        pass

    def test_if_page_response_has_a_error_such_as_could_not_be_found(self):
        # I've seen an awful lot where there will be content returned but it's an invalid response for our purposes
        # Could be as simple as checking for the name and certain other fields
        pass

    def test_if_page_reponse_has_text_we_are_looking_for(self):
        # We have to make sure that the page actually contains what we need in order to get our information, in this case
        # It is the number of visits in 60 days
        pass

