-- SELECT * FROM artists;
-- select title,name
-- from albums 
--   join artists
--   on albums.artistid=artists.artistid
-- limit 30;


-- select 
--   sum(tr.milliseconds) as total_millisecond,
--   ar.name as artist_name
  
-- FROM
--   artists as ar 
-- join 
--   albums as al 
-- on ar.artistid = al.artistid
-- JOIN
--   tracks as tr
-- on tr.albumid = al.albumid
-- GROUP BY ar.artistid;




select 
  playlists.playlistid,
  playlists.name,
  sum(tracks.unitprice) as total_price
from playlists 
join  playlist_track on playlists.playlistid = playlist_track.playlistid
JOIN tracks on  tracks.trackid = playlist_track.trackid
GROUP by playlists.playlistid
order by total_price;