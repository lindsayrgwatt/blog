Title: How To Update Arrays of Javascript Objects
Date: 2011-02-04 17:36
Author: lindsayrgwatt
Category: Technology
Tags: coding, howto, javascript
Slug: how-to-update-arrays-of-javascript-objects
Status: published

I've been doing some front-end web development and a common situation has come up again and again:

- You've request a set of objects from a server (json or xml)
- You store them in an array
- The user does something
- You need to request a changed set of objects and update that array

You've got two options here:

1.  Destroy the original array (and create all new objects)
2.  Loop through the original array to remove objects that aren't in the new set and then add objects from the new set that aren't in the original

Frequently option 1 isn't *really* an option because destroying the original object would cause a negative experience for the end user. For instance, the screen might flash as everything they had chosen to see was temporarily destroyed and re-created.

As a result, you've got to take option 2. As a Javascript noob, it took me a bit of time and reading a lot of tutorials to figure out the best way to do it.

To help you avoid suffering my fate, I've created a quick demo of how to do it. Simply save the code below as an html file and you'll get walked through a demo on how to do it.

```



    A Javascript Test
    
        function DisplayPropertyNamesAndValues(obj) {
            var names = "";
            for(var name in obj) names += name + " :: " + obj[name] + "\n";
            alert(names);
        }
        
        function DisplayArrayPropertyNamesAndValues(arr) {
            var results = "";
            for (var i=0; i<arr.length; i++) {
                for(var name in arr[i]) results += name + " :: " + arr[i][name] + ", "; 
                results += "\n";
            }
            alert(results);
        }
        
        // Two array full of same type of objects
        var locations = [{'location':'Granville Island','id':1}, {'location':'Home','id':3}, {'location':'49th Parallel','id':6}, {'location':'Cafe Mei Mei','id':10}, {'location':'Siegel\'s Bagels','id':2}, {'location':'The Diamond','id':22}];
        var places = [{'location':'Shiftyville','id':4}, {'location':'Cafe Mei Mei','id':10}, {'location':'Cooperstown','id':32}, {'location':'Black Jack\'s','id':7}, {'location':'Siegel\'s Bagels','id':2}, {'location':'Starbucks','id':8}, {'location':'One More Place','id':9}];
        
        // Create new arrays that are just the ids within each array. Index of id corresponds to same location in original array
        // Create a new object to store the location ids
        // Each id is a property of the object. The value of the property is the corresponding index in the array
        var locations_id = {};
        var id_holder = 0;
        for (var i=0; i<locations.length; i++) {
            id_holder = locations[i]['id'];
            locations_id[id_holder] = i;
        }
        // Enumerate object and alert
        DisplayPropertyNamesAndValues(locations_id);
        
        var places_id = {};
        for (var i=0; i<places.length; i++) {
            id_holder = places[i]['id'];
            places_id[id_holder] = i;
        }
        
        // Enumerate object and alert
        DisplayPropertyNamesAndValues(places_id);
        
        // Now loop through locations_id and find all the locations that don't exist in places_id
        // Create an array storing the index of each place that doesn't exist
        // We'll come back and delete these
        var locations_to_remove = []
        for (var name in locations_id) {
            if (places_id[name] === undefined) {
                locations_to_remove.push(locations_id[name]);
            }
        }
        // Sort the array just in case there's a chance it's out of order
        // Important as we're going to go backwards through the array to later remove items
        locations_to_remove.sort();
        alert("Need to remove the following from locations_id: " + locations_to_remove);
        
        // Do the similar for places_id and locations_id
        // Difference this time is that we want to remove any pre-existing locations from places_id
        // Note that change in the equality operator
        var places_to_remove = []
        for (var name in places_id) {
            if (locations_id[name] !== undefined) {
                places_to_remove.push(places_id[name]);
            }
        }
        places_to_remove.sort();
        alert("Need to remove the following from places_id: " + places_to_remove);
        
        // Now splice out the elements from their respective arrays
        for (var i=locations_to_remove.length-1; i>=0; i--) {
            locations.splice(locations_to_remove[i],1);
        }
        DisplayArrayPropertyNamesAndValues(locations);
        
        for (var i=places_to_remove.length-1; i>=0; i--) {
            places.splice(places_to_remove[i],1);
        }
        DisplayArrayPropertyNamesAndValues(places);
        
        // Now add the remaining elements in places to locations
        for (var i=0; i<places.length; i++) {
            locations.push(places[i]);
        }
        DisplayArrayPropertyNamesAndValues(locations);
    



```
