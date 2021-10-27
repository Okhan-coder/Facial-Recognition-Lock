import json
import requests

if __name__ == '__main__':
   
    url = "https://hooks.slack.com/services/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"
    headers = {'Content-Type': "application/json"}

   
    message = ("There is someone at the main door")
    title = (f"Check the main door :bell:")
   
    data = {
     "username": "LockBot",
     "icon_emoji": ":closed_lock_with_key:",
     "text": "There is someone at your door :bell:",
   
    "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "There is someone at the Door :bell:"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "plain_text",
        "text": "Would you like to let them in?"
      }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Allow :unlock:"
          },
          "style" : "primary",
          "value": "click_me_123",
          "url": "https://www.google.com/search?q=allow"
        },
        {
          "type": "button",
          "text": {
            "type": "plain_text",
            "text": "Deny :lock:"
          },
          "style" : "danger",
          "value": "click_me_123",
          "url": "https://www.google.com/search?q=deny"
        }
      ]
    },
    {
      "type": "divider"
    }
  ]
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.status_code)
