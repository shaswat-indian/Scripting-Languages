window.onload=function()	{

	teslaModels=[
			{
				"name":"Model 3",
				"model":"model3",
				"price":"1500",
				"year":"2017"
			},

			{
				"name":"Model S",
				"model":"models",
				"price":"1600",
				"year":"2018"
			},

			{
				"name":"Model X",
				"model":"modelx",
				"price":"2500",
				"year":"2015"
			}
		];


	teslaModels.forEach(function(item,index)	{

		elem=document.createElement("th");
		elem.id=item.model;
		elem.innerHTML=item.name;
		document.getElementById("menu").appendChild(elem);

	})

	
	teslaModels.forEach(mouseEventHandler);

	function mouseEventHandler(item,index)	{

		elem=document.getElementById(item.model);
		elem.onmouseover=function ()	{
		
			details=item;
			document.getElementById("data-elements").removeAttribute("hidden");
			document.getElementById("name").innerHTML=details.name;
			document.getElementById("picture").innerHTML='<img src="img/'+details.model+'.png">';
			document.getElementById("price").innerHTML="$"+details.price;
			document.getElementById("year").innerHTML=details.year;
			

		}
	}











};
