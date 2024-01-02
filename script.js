function getresults()
  {
    var link = document.resultform.url.value
    try{
    var start = BigInt(document.resultform.start.value)
    var end = BigInt(document.resultform.end.value)
    }
    catch(err)
    {
      alert("Roll numbers seem incorrect")
    }
    
  }

function getrollnum()
  {
    try{
    var rollnum = BigInt(document.rollform.rollno.value)
    var semester = Number(document.rollform.sem.value)}
    catch(err){alert("Roll number/Semester is incorrect")}
    $.ajax({
      url: "hello.py",
       context: document.body
      })

  }