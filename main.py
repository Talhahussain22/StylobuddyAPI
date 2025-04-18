from gradio_client import Client

client = Client("Talha2005/stylobuddy")
result = client.predict(
		shirts="https://static.vecteezy.com/system/resources/thumbnails/046/829/943/small/yellow-t-shirt-isolated-on-transparent-background-png.png",
		pants=" https://static.vecteezy.com/system/resources/thumbnails/057/716/439/small/elegant-formal-pant-in-black-and-gray-tones-for-professional-attire-and-corporate-wardrobe-png.png",
		api_name="/predict"
)
print(result)
