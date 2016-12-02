/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function getSearchData()
{
    var begin_time = document.getElementById('start-datetime').value;
    var end_time = document.getElementById('end-datetime').value;
    var keywords = document.getElementById('keyboard').value;
    var condition = document.getElementById('show').value;
    var status = document.getElementById('status').value;
    var url = "/index.php?r=appAdmin/logs/getsearchdata/";
    requestData = {'begin_time': begin_time, 'end_time': end_time,'keywords':keywords,'condition':condition,'status':status};
    $(".table-content").remove();
    $.post(url, requestData, function(data) {
        if(data)
        {
            var return_data = eval('('+data+')');
            $(".table-content").html("");
            var result = "";
            for(var i=0;i<return_data.length;i++)
            {
                result += "<tr id='logid_"+return_data[i].id+" 'class='table-content' style='padding: 5px;'>";
                result += "<th align='center' style='width:7%'><div align='center'>"+return_data[i].id+"</div></th>";
                result += "<th style='width:28%' align='center'><div align='center'>"+return_data[i].user+"</div></th>";
                status = return_data[i].status==1 ? '登录成功': "<span style='color:red'>密码错误</span>";
                result += "<th style='width:20%'><div align='center'>"+status+"</div></th>";
                result += "<th style='width:17%'><div align='center'>"+return_data[i].login_ip+"</div></th>";
                result += "<th style='width:17%'><div align='center'>"+return_data[i].login_time+"</div></th>";
                result += "<th style='width:11%'>";
                result += "<div align='center'><a class='del-checkbox' onclick=return&nbsp;delLogId("+return_data[i].id+") href='javascript:void(0);' ></a>&nbsp;<input type='checkbox' name='logId' value='"+return_data[i].id+"'></div>";
                result += "</tr>";
            }
            $(".header").after(result);
        }else{
            location.href="/index.php?r=appAdmin/index/index";
        }
    });
}

