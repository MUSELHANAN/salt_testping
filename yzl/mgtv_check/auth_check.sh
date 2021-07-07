#! /bin/bash
if [ x"$1" = x ];
then
echo "请输入参数!"
exit 1
fi

authinfo=`salt $1   cmd.run "/home/postgres/pgsql/bin/psql zxin zxcdn_webcache -c \"select authid from authinfo_policy where templateid='mgtvvideo'\"" |grep 100`
echo $authinfo
