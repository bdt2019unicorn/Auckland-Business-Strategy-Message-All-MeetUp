// ************************

var scroll_down = function(index)
{
	return new Promise 
	(
		(resolve,reject)=>
		{
			if(index>=4)
			{
				reject(); 
			}
			else 
			{
				setTimeout
				(
					function()
					{
						console.log(index); 
						var ul = document.querySelector("#member-list-card-id > div:nth-child(3) > div > ul");
						ul.scrollIntoView(false); 
						resolve(index+1); 
					}, 
					5000
				); 
				
			}
		}
	).then(scroll_down); 
}

var load_more_member = function(count)
{
	return new Promise
	(
		(resolve, reject)=>
		{
			if(count>=5504)
			{
				reject(); 
			}
			else 
			{
				var ul = document.querySelector("#member-list-card-id > div:nth-child(3) > div > ul");
				var more_members_button = document.querySelector("#member-list-card-id > div:nth-child(3) > div.padding--bottom.align--center.border--top.padding--top-double > button");
				ul.scrollIntoView(false); 
				window.scrollBy(0,100); 
				more_members_button.click(); 
				setTimeout
				(
					function()
					{
						count = ul.childElementCount; 
						console.log(count); 
						resolve(count); 
					}, 5000
				); 
			}
		}
	).then(load_more_member); 
}

var chain = async function()
{
	try 
	{
		var chain = await scroll_down(0); 
	}
	catch 
	{
		try 
		{
			var chain = await load_more_member(0); 
		}
		catch {}
	}
}

chain(); 

// ***********************************


// ?????????????????????

var ul = document.querySelector("body > ul");
var list = ul.querySelectorAll("li"); 
var new_ul = document.createElement("ul"); 
var links = []; 
list.forEach 
(
	function(li)
	{
		var message = li.querySelector("div > div.flex-item.flex-item--shrink.member-item-menu > ul > div");
		if(message.childElementCount>0)
		{
			var a = message.querySelector("div > a"); 
			links.push(a.href); 
			new_ul.append(li); 
		}
	}
);
console.log(new_ul); 
console.log(links); 



// ?????????????????????????