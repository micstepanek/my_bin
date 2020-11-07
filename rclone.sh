#!/bin/bash
echo rclone working ...

rclone sync ~/aa remote:aa -vul
rclone sync ~/aa/rclone_links/ remote:not_aa -vuL

#rclone sync ~/aa/bin/ remote:bin -vul
#rclone sync ~/aa/sync_links/ remote:sync_links -vul
#rclone sync ~/aa/path_links/ remote:path_links -vul
#rclone sync ~/aa/my_links/ remote:my_links -vul
#rclone --max-depth 1 sync ~/aa remote:aa -vul

echo done
