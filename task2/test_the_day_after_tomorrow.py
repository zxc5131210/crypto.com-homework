import json
import api_requests
import utils


def task2():
    data = api_requests.ApiRequest().get_response()
    day_after_tomorrow = utils.get_day_after_tomorrow()

    # Save the received data into a json file
    with open("weather_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    forecast = next(
        (
            item
            for item in data["forecast_detail"]
            if item["forecast_date"] == day_after_tomorrow
        ),
        None,
    )
    min_rh = forecast["min_rh"]
    max_rh = forecast["max_rh"]

    if forecast:
        print(
            f"the day after tomorrow's ({day_after_tomorrow}) relative humidity is {min_rh}-{max_rh}%"
        )
    else:
        print("No forecast data for the day after tomorrow")


if __name__ == "__main__":
    task2()
