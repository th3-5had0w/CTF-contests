<?php
    error_reporting(0);

    // Create folder for each user
    session_start();
    if (!isset($_SESSION['dir'])) {
        $_SESSION['dir'] = 'upload/' . bin2hex(random_bytes(16));
    }
    $dir = $_SESSION['dir'];
    if ( !file_exists($dir) )
        mkdir($dir);

    if(isset($_FILES["file"])) {
        $error = '';
        $success = '';
        try {
            $file = $dir . "/" . urldecode($_FILES["file"]["name"]);
            move_uploaded_file($_FILES["file"]["tmp_name"], $file);
            $success = 'Successfully uploaded file at: ' . $file;
        } catch(Exception $e) {
            $error = $e->getMessage();
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>Kid Drive</title>

        <!-- This is for UI only -->
        <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.0/css/bootstrap.min.css" integrity="sha512-P5MgMn1jBN01asBgU0z60Qk4QxiXo86+wlFahKrsQf37c9cro517WzVSPPV1tDKzhku2iJ2FVgL67wG03SGnNA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        <link href="https://unpkg.com/nes.css@2.3.0/css/nes.min.css" rel="stylesheet" />
        <style> 
            input {
                cursor: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAzElEQVRYR+2X0Q6AIAhF5f8/2jYXZkwEjNSVvVUjDpcrGgT7FUkI2D9xRfQETwNIiWO85wfINfQUEyxBG2ArsLwC0jioGt5zFcwF4OYDPi/mBYKm4t0U8ATgRm3ThFoAqkhNgWkA0jJLvaOVSs7j3qMnSgXWBMiWPXe94QqMBMBc1VZIvaTu5u5pQewq0EqNZvIEMCmxAawK0DNkay9QmfFNAJUXfgGgUkLaE7j/h8fnASkxHTz0DGIBMCnBeeM7AArpUd3mz2x3C7wADglA8BcWMZhZAAAAAElFTkSuQmCC) 14 0,pointer !important
            }
        </style>
    </head>
    <body>
        <br/>
        <br/>
        <h3 class="nes-text text-center">Kid CTF drive</h3>
        <h4 class="nes-text text-center">We store everything in the world</h4>

        <br/>
        <div class="container">
            <a class="nes-text" href="/source">Debug source</a>
            <form method="post" enctype="multipart/form-data">
            <label class="nes-btn">
                <span>Select your file</span>
                <input type="file" name="file" id="fileInp">
            </label>
            <br>
            <span id="fileName" class="nes-text"></span>
            <br><br>
            <input type="submit" class="nes-btn is-primary">
            </form>
            <span style="color:red"><?php echo $error; ?></span>
            <span style="color:green"><?php echo $success; ?></span>
        </div>
        <script>
            function showFileName(e) {
                fileName.innerText = event.srcElement.files[0].name;
            }
            fileInp.addEventListener("change", showFileName);
        </script>
    </body>
</html>
