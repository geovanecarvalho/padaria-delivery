function form_client(){
    first_name = document.querySelector("#id_first_name");
    last_name = document.querySelector("#id_last_name");
    date_of_birth = document.querySelector("#id_date_of_birth");
    cpf = document.querySelector("#id_cpf");
    phone_number = document.querySelector("#id_phone_number");
    address = document.querySelector("#id_address");

    first_name.value = ""
    last_name.value = ""
    date_of_birth.value = ""
    cpf.value = ""
    phone_number.value = ""
    address.value = ""
}

function form_product(){
    image = document.querySelector("#id_image");
    product = document.querySelector("#id_name");
    amount = document.querySelector("#id_amount");
    value_item = document.querySelector("#id_value");
    description = document.querySelector("#id_description");
    
    image.value = ""
    product.value = ""
    amount.value = ""
    value_item.value = ""
    description.value = ""
}