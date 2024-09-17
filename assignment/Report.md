Results of post request: https://i.postimg.cc/pr9qKP26/image.png

1 minute video of post results: https://photos.app.goo.gl/uSW5W2dEqWdWJuAS8

We first tried to make a web server with a login, but encountered some errors. We then pivoted to upload to firebase since it was recommended. Before realizing our errors were happening because of library importing issues with the Pico, we switched to using Webhook.site for our post request to simplify things. The problems were mainly due to micropython libraries requiring mip instead of upip, which most online resources said was useful but has since been discontinued.

