import qrcode as qr
img=qr.make("https://ai-realtime-physical-trainer.netlify.app/")
img.save("physical_trainer.png")