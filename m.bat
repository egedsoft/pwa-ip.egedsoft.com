curl -X POST -H "Authorization: key=AIzaSyCm9FdLLNY7cGh1R-0qdb1hdfbs6Xvf1cI" -H "Content-Type: application/json" -d '{
  "notification": {
    "title": "Hello World PWA",
    "body": "Hi",
  },
  "to": "DEVICE_REGISTRATION_TOKEN"
}' "https://fcm.googleapis.com/fcm/send"