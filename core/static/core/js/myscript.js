
$('.delete-data').click(function(){
    var id = $(this).attr("pid").toString();
    var eml=document.getElementById('table-row');
    $.ajax({
        url:"/deletdoctor",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(id)
            eml.remove()     
        }
    });
});
$('.delete-data').click(function(){
    var id = $(this).attr("pid").toString();
    var eml=document.getElementById('table-row');
    $.ajax({
        url:"/deletpatient",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(id)
            eml.remove()     
        }
    });
});
$('.delete-data').click(function(){
    var id = $(this).attr("pid").toString();
    var eml=document.getElementById('table-row');
    $.ajax({
        url:"/deletroom",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(id)
            eml.remove()     
        }
    });
});
$('.delete-data').click(function(){
    var id = $(this).attr("pid").toString();
    var eml=document.getElementById('table-row');
    $.ajax({
        url:"/deletlab",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(id)
            eml.remove()     
        }
    });
});
$('.edit-data').click(function(){
    var id = $(this).attr("pid").toString();
    var eml=document.getElementById('table-row');
    $.ajax({
        url:"/updatedoctor",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(id) 
        }
    });
});
$('.done').click(function(){
    var id = $(this).attr("pid").toString();
    $.ajax({
        url:"/appointmentaccept",
        data:{
            prod_id:id
        },
        success:function(data){
            alert(data.value)
        }
    });
});