<?php

require_once("../model/model.php");

    $query = "select legislator_id, first_name, last_name, photo from gadb_legislator";
    $result = mysql_query($query) or die();


    while ($row = mysql_fetch_assoc($result)){
        print "Name is " . $row['first_name'] . " and photo is " . $row['photo'] . "\n";
        preg_match("/\/(\d+)\.jpg$/", $row['photo'], $leg_id);
        print_r($leg_id);
        $id = $leg_id[1];

        file_put_contents("/content/www/rollcall/legislator_images/$id.jpg", file_get_contents($row['photo']));

        $legislator_id = $row['legislator_id'];
        $photo = "/rollcall/legislator_images/$id.jpg";
        $update_query = "update gadb_legislator set photo='$photo' where legislator_id='$legislator_id'";
     
        print "$update_query\n";
        mysql_query($update_query) or die($update_query . mysql_error());

    }



//$id = mysql_insert_id();
//file_put_contents($_SERVER['DOCUMENT_ROOT'] . "/ga_db/legislator_images/$id.jpg", file_get_contents($image));
//file_put_contents("/content/www/rollcall/legislator_images/$id.jpg", file_get_contents($image));
//$query = "UPDATE gadb_legislator SET photo = '/ga_db/legislator_images/$id.jpg' WHERE legislator_id='$id'";
//mysql_query($query) or die($query . mysql_error());
        


?>
