$(document).ready(function () {
    $('.payWithRazorpay').click(function (e) {

        e.preventDefault();
        

        var Fname=$(" [name='Fname']").val();
        var Lname=$(" [name='Lname']").val();
        var Phone=$(" [name='Phone']").val();
        var Address=$(" [name='Address']").val();
        var City=$(" [name='City']").val();
        var State=$(" [name='State']").val();
        var Pincode=$(" [name='Pincode']").val();
        var token=$("[name=csrfmiddlewaretoken]").val();

        if (Fname == "" || Lname=="" || Phone == "" || Address == "" || City=="" || State == "" || Pincode=="") {
            alert("All fields are mandatory");
            return false ;
        }
        else
        {
            $.ajax({
                method:"GET",
                url:'/Dashboard/razorpaycheck',
                // url:"/Dasboard/razorpaycheck/",
                success:function(response){

                    console.log(response)
                    var options = {
                        "key": "rzp_test_GwV3Og3iKv58qn", // Enter the Key ID generated from the Dashboard
                        "amount": response.total_price * 100,// Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Aceme Corp" , //your business name
                        "description": "Thank You for buying",
                        "image": "https://example.com/your_logo",
                        
                        // "notes": {
                        //     "address": "Razorpay Corporate Office"
                        // },
                       
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function(responseb){
                            // alert(responseb.razorpay_payment_id)
                        
                            alert(responseb.razorpay_payment_id);
                            
                            data={
                                "Fname":Fname,
                                "Lname":Lname,
                                "Phone":Phone,
                                "Address":Address,
                                "City":City,
                                "State":State,
                                "Pincode":Pincode,
                                "payment_id":responseb.razorpay_payment_id,
                                csrfmiddlewaretoken:token
    
                            } 

                            $.ajax({
                                method:"POST",
                                url:'/Dashboard/CheckOut',
                                data:data,
                                success:function(responsec){
                                    // swal("congrats",responsec.status)
                                    alert(responseb.razorpay_payment_id);
                                    var url = "{% url 'dashboard:myOrders' }";
                                    window.location.href= '/Dashboard/myOrders/'
                                    // url + "/" + request.session.cart;
                                    //   '==

        
                                    
                                }
                            });
                            
                        },
                        "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                            "name": Fname+" "+Lname, //your customer's name
                            "email": "gaurav.kumar@example.com", 
                            "contact": "9999999999"  //Provide the customer's phone number for better conversion rates 
                        },
                        "theme": {
                            "color": "#3399cc"
                        },
                       
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                    e.preventDefault();
                    
                    
                    
                    
                }
            });
            
        }

        
        
    

       
            
           

        

    

       


    });
});