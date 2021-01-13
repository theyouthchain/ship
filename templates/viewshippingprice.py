


<!DOCTYPE html>  
<html>  
<head>  
    <title>List</title>  
</head>  
<body>  
  
<h3>SHIPPINGPRICE Information</h3>  
<table border=5>  
    <thead> 
 	<td>ID</td> 
        <td>idpricelist</td>    
        <td>idprovince</td>  
        <td>idsupplier</td>  
        <td>five</td>
        <td>fifty</td>
        <td>hundred</td>
        <td>onetwenty</td>
        <td>fixed</td>
        <td>insurance</td>
        <td>insmin</td>
    </thead>  
      
    {% for row in rows %}  
      
        <tr>  
            <td>{{row["idpricelist"]}}</td>  
            <td>{{row["idprovince"]}}</td>  
            <td>{{row["idsupplier"]}}</td>  
            <td>{{row["five"]}}</td> 
    	    <td>{{row["fifty"]}}</td>
    	    <td>{{row["hundred"]}}</td>
    	    <td>{{row["onetwenty"]}}</td>
    	    <td>{{row["fixed"]}}</td>	
    	    <td>{{row["insurance"]}}</td>
    	    <td>{{row["insmin"]}}</td> 