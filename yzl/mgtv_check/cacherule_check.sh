#! /bin/bash
if [ x"$1" = x ];
then
echo "请输入参数!"
exit 1
fi

cache_rule=`salt $1   cmd.run "/home/postgres/pgsql/bin/psql zxin zxcdn_webcache -c \"select domain from cache_rule\"" |grep mgtv`
echo $cache_rule
