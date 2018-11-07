<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        % if request.get_cookie("vara"):
            % valin_vara = request.get.cookie("vara")
        % end
        {{valin_vara}}
    </body>
</html>