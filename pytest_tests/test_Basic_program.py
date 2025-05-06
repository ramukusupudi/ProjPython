

import pytest
from  project_main import Basic_program 

class TestFormatDate:

    # Format a valid date string with default input format
    def test_format_valid_date_with_default_format(self):
        from datetime import datetime
    
        # Call the function with a valid date string
        result = Basic_program.format_date("2023-05-15")
    
        # Check that all expected formats are returned
        assert "ISO 8601" in result
        assert result["ISO 8601"] == "2023-05-15T00:00:00"
        assert result["DD-MM-YYYY"] == "15-05-2023"
        assert result["MM/DD/YYYY"] == "05/15/2023"
        assert result["Month Day, Year"] == "May 15, 2023"
        assert result["Day-Month-Year (Short)"] == "15-May-23"
        assert result["Weekday, DD Month YYYY"] == "Monday, 15 May 2023"
        assert result["Custom 1"] == "2023/05/15 00:00:00"
        assert result["Custom 2"] == "15-05-2023 12:00 AM"

    # Handle invalid date strings that don't match the input format
    def test_handle_invalid_date_string(self):
        from datetime import datetime
    
        # Call the function with an invalid date string
        result = Basic_program.format_date("2023/05/15")
    
        # Check that an error is returned
        assert "error" in result
        assert "Invalid date or format" in result["error"]
