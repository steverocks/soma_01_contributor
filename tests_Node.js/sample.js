const express = require("express");
const crypto = require("crypto");

const app = express();

let dummy = Object();


app.use("/api/:url", (req, res) => {

    let is_err = 0;

    crypto.randomBytes(32, function(err, buffer){//추가된 32바이트는 버퍼 파라미터로 전달


        if (err){
            console.log(err);
            is_err = 1;
        } else{
            //에러가 없을 때, 즉 성공적으로 32바이트가 생성됐을 때
            //샤512로 해싱
            crypto.pbkdf2(req.params.url, "", 1, 12, "sha512", function(err, hashed){ //해싱된 결과를 hashed 파라미터로 전달
                if (err){
                    console.log(err);
                    is_err = 1;
                    res.end(JSON.stringify({ //json 객체 생성
                        isError:is_err,
                        errorMessage:err,
                        restShortUrl: "NULL"
                    }))
                } else{
                    //에러가 없을 때, 클라이언트로 관련 도큐먼트 전달

                    res.statusCode = 200; //성공
                    res.setHeader("Content-Type", "application/json"); //json 객체로 전달
                    res.end(JSON.stringify({ //json 객체 생성
                        isError:is_err,
                        errMessgage:"No Error",
                        restShortUrl: "soma.short/"+hashed.toString("base64")
                    }))

                    dummy[req.params.url] = hashed.toString("base64");

                    console.log(dummy);


                }
            })
        }

    });
});

app.use((req, res) => {
    res.send("Not Found");
})

app.listen(3000, ()=>console.log("3000!"));
