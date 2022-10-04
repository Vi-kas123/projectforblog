$(document).ready(function(){
//       alert("first")
        $.getJSON('http://localhost:8000/fetch_all_blogs',function(data){
       htm=''
       data.data.map(item=>{
         var data=JSON.stringify(item)
         htm+=`<a href='http://localhost:8000/blog_description?blog=${data}' style="text-decoration: none;color: black;" ><div style="display: flex; flex-direction: column; margin: 10px;align-items: center; width: 250px; height: 300px; padding: 5px; border: 1px solid #bdc3c7;box-shadow: 2px 2px #ecf0f1;elevation: below;border-radius: 10px;">
      <div><img src="http://localhost:8000/static/${item.blogimage}" style="width: 150px;height: 150px;"></div>

      <div style="padding: 5px; display: flex;">
         <div style="font-weight: bolder;width:200px;text-align:left;">${item.title}</div>
      </div>
      <div style="width:200px;text-align:left;font-size:10px;"><i>Type : ${item.blogtype}</i></div>
         <div style="font-weight: bolder;width:200px;text-align:left;font-color: blue">Click To Know More</div>





      </div></a>`
     })
       $('#bloglist').html(htm)
     })




})