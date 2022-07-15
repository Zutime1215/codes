<?php 
$new_backup = array(
    'Title' => $_GET['Title'],
    'Description' => $_GET['Description'],
    'Username' => $_GET['Username'],
    'Password' => $_GET['Password'],
    'Others' => $_GET['Others']
);

$file_name = $_GET['iD']. '.json';

if(isset( $_GET['touch'] ))
{
	file_creator( $_GET['iD'] );
} elseif( isset($_GET['Title'])  && isset($_GET['Password']) ){
	
	if(filesize($file_name) == 0){

		$first_record = array($new_backup);
		$data_to_save = $first_record;

	}else{

		$old_records = json_decode(file_get_contents($file_name));
		array_push($old_records, $new_backup);
		$data_to_save = $old_records;

	}
	if(!file_put_contents($file_name, json_encode($data_to_save, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE), LOCK_EX)){
		$error = "Error";
	}else{	
		$success =  "successful";
	}
}

function file_creator($fileName) {
    $file=fopen($fileName. '.json',"w");
    fwrite($file, "");
    fclose($file);
}
?>