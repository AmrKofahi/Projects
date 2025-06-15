<?php 

    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $email = $_POST['email'];
    $reason = $_POST['reason'];
    $message = $_POST['message'];



    setcookie("user",$fname .' ' . $lname,time()+(5*86400),"/");
    setcookie("email",$email,time()+(5*86400),"/");


    //RDBMS
    $servername = "localhost";	
    $username = "username";	
    $password = "password";	
    $dbname = "myDB";	
    
    // Create connection 	
    $conn = new mysqli($servername, $username, $password, $dbname);
	
	
    
    //data insert

    $sql = "INSERT INTO Contacts (fname,lname,email,reason,message)
    VALUES ('$fname','$lname','$email','$reason','$message')";

    if($conn->query($sql)==TRUE {
        echo "New record created successfully";
    }
    else {
        echo "Error: " .$sql . "<br>" .$conn->error;
    }

    //retrieve date from table

    $sql= "SELECT * FROM mytable";
    $result= $conn->query($sql);

    if($result->num_rows>0){
        while($row=$result->fetch_assoc())
        {
        echo " - Name: " . $row["firstname"] . " " . $row["lastname"];
        echo " - Email: " . $row["email"];
        echo " - Reason: " . $row["reason"];
        echo "<br>";	

        }
    } else {
        echo "no records found.";
    }

    $conn->close();
?>