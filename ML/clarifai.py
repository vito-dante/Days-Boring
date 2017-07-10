from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


# - `CLARIFAI_APP_ID`
# - `CLARIFAI_APP_SECRET`

app = ClarifaiApp()

app = ClarifaiApp("{ID}", "{SECRET}")


data['outputs'][0]['data']['concepts']

from clarifai.rest import ClarifaiApp

app = ClarifaiApp("sHDfq9nyBpkBvi2zPZAvGPR0mjnk8I7oEmciktQb", "raTGTWiJFfiX6ULfGsP26IKohHnerz9Q_b0sEdAp")

# import a few labeld images
app.inputs.create_image_from_url(url="https://www.rover.com/blog/wp-content/uploads/2015/04/boo-pomeranian.jpg", concepts=["cute dog"], not_concepts=["cute cat"])
app.inputs.create_image_from_url(url="http://cdn2.ubergizmo.com/wp-content/uploads/2012/08/boo-the-dog.jpg", concepts=["cute dog"], not_concepts=["cute cat"])

app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat1.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat2.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])

model = app.models.create(model_id="pets", concepts=["cute dog"])

model = model.train()

# predict with samples
print model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg")
print model.predict_by_url(url="https://samples.clarifai.com/cat3.jpeg")
