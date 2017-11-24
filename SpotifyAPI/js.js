
// browserify js.js -o bundle.js
// Don't forget to run browerify to get the bundle.js

var SpotifyWebApi = require('spotify-web-api-js');

var spotifyApi = new SpotifyWebApi({
  clientId : 'dfd789f848ac45dab9aafe737f717abc',
  clientSecret : 'fed50c0b74014e338f49d5416ac3ef9d',
  redirectUri : 'http://localhost:8888/callback'
});

//get all albums from artist
  spotifyApi.setAccessToken('BQDZOSeryDWrr9RmVqMCcLCzaeEbP_qdoenSYFpGFuL7_Y0XfUvglA6nZah3PJcBGv2PCJ7jYGkJmZ9hfrHZOEkjj6BF6ZxZ2DUAt1cyY8pIK4eMXYdoCxYgPIVBAKeKiYZWBVx0sGw2gHAX8R-DbkFRohFqAJI');
  spotifyApi.getArtistAlbums('43ZHCT0cAZBISjO8DG9PnE', function(err, data) {
    if (err) console.error(err);
    else console.log('Artist albums', data);
  });

//get album
spotifyApi.getAlbum('2QJmrSgbdM35R67eoGQo4j', function(err, data) {
  if (err) console.error(err);
  else console.log('Album: ', data);
});


//get track
spotifyApi.getTrack('3Qm86XLflmIXVm1wcwkgDK', function(err, data) {
  if (err) console.error(err);
  else console.log('Track:', data);
  //print album of track
  //console.log("This track is from this album: ", data["album"]["id"])
});

spotifyApi.getArtist('06HL4z0CvFAxyc27GXpf02', function(err, data) {
  if (err) console.error(err);
  else console.log('Artist: ', data);
})
