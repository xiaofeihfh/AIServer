import time

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from server.models import License
from utils.util import decrypt


# Create your views here.
class CheckProject(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'msg': 'check'})

    def post(self, request):
        start_time = time.time()  # 开始计时
        data = request.data
        encrypted_machine_code = data.get('machine_code')
        encrypted_version = data.get('version')

        if not encrypted_machine_code or not encrypted_version:
            return Response({'error': '缺少机器码或版本信息'}, status=400)
        machine_code = decrypt(encrypted_machine_code)
        version = decrypt(encrypted_version)
        decrypt_time = time.time()  # 记录解密后的时间
        license_db, status = License.objects.get_or_create(machine_code=machine_code)
        db_query_time = time.time()  # 记录数据库查询结束时间
        db_insert_time = time.time()  # 记录数据库插入结束时间

        response = {
            'expiration_date': license_db.expiration_date.strftime('%Y-%m-%d'),
            'remaining_days': license_db.remaining_time(),
            'user_permission': license_db.user_permission  # 返回用户权限信息
        }

        total_time = time.time() - start_time  # 总耗时
        print(f"解密耗时: {decrypt_time - start_time:.4f} 秒")
        print(f"数据库查询耗时: {db_query_time - decrypt_time:.4f} 秒")
        print(f"数据库插入耗时: {db_insert_time - db_query_time:.4f} 秒")
        print(f"总耗时: {total_time:.4f} 秒")

        return Response(response)
