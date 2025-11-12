import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function that divides two numbers.

    Expected event:
    {
      "numerator": 10,
      "denominator": 2
    }
    """
    try:
        numerator = event.get("numerator")
        denominator = event.get("denominator")

        if numerator is None or denominator is None:
            raise ValueError("Both 'numerator' and 'denominator' must be provided.")

        result = numerator / denominator  # may raise ZeroDivisionError

        message = f"Division successful: {numerator} / {denominator} = {result}"
        logger.info(message)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "result": result,
                "message": message
            })
        }

    except ZeroDivisionError:
        error_msg = "Error: Division by zero is not allowed"
        logger.error(error_msg)
        return {
            "statusCode": 400,
            "body": json.dumps({"error": error_msg})
        }

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

handler = lambda_handler
