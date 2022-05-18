<?php

$sql
=
"
INSERT INTO asdasdas (asdasd, qweqew`)
VALUES (:nombre, :value_two)
"
;

try
{
    
    $core = Core::getInstance();
    $stmt = $core->dbh->prepare($sql);
    $stmt->bindParam(':nombre', $value_one, PDO::PARAM_INT);
    $stmt->bindParam(':value_two', $value_two, PDO::PARAM_STR);
    
    if ($stmt->execute())
    {
        
        $stmt = null;
        $core = null;
        
        
        
    } else { echo 'Couldn\'t connect to DB'; }
    
} catch(PDOException $e) { echo $sql . "<br>" . $e->getMessage(); }

?>