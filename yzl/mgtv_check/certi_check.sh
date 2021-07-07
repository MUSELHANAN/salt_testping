#! /bin/bash
if [ x"$1" = x ];
then
echo "请输入参数!"
exit 1
fi

certi=`salt $1   cmd.run "/home/postgres/pgsql/bin/psql zxin zxcdn_slb -c  \"select distinct domain from certificate_cfg where domain like '%mgtv%' order by domain\""|grep mgtv`
echo $certi
