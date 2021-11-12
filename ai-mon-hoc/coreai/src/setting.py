IMAGE_HEIGHT = 128
IMAGE_WIDTH = 128
BATCH_SIZE = 64
CLASS = [
    {
        "id":"U_0901c348-3513-4607-9a5b-f4ac44dfa07f",
        "ten": "QuangHieu"
    },
    {
        "id":"U_94ab6f08-8d40-4e68-b328-f9f1de4a52ab",
        "ten": "Hue"
    },
    {
        "id":"U_8e63a5e1-590a-4010-a60e-670295114724",
        "ten": "Nhung"
    }
  ]
CLASS_DIST = dict()
for count, i in enumerate(CLASS):
    CLASS_DIST[i["id"]] = int(count)