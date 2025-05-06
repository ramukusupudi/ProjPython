import datetime

now =datetime.now()
print("current date and time:,now")
formted =now.strftime("%Y-%m-%d %H:%M:%S")

def format_date(date_str, input_format="%Y-%m-%d"):
    try:
        date_obj = datetime.strptime(date_str, input_format)
        
        formats = {
            "ISO 8601": date_obj.isoformat(),
            "DD-MM-YYYY": date_obj.strftime("%d-%m-%Y"),
            "MM/DD/YYYY": date_obj.strftime("%m/%d/%Y"),
            "Month Day, Year": date_obj.strftime("%B %d, %Y"),
            "Day-Month-Year (Short)": date_obj.strftime("%d-%b-%y"),
            "Weekday, DD Month YYYY": date_obj.strftime("%A, %d %B %Y"),
            "Custom 1": date_obj.strftime("%Y/%m/%d %H:%M:%S"),
            "Custom 2": date_obj.strftime("%d-%m-%Y %I:%M %p")
        }

        return formats
    except ValueError as e:
        return {"error": f"Invalid date or format: {e}"}