from App.moduels import Category, Product, UserRoleEnum
from App import app, db
from flask_admin import  Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView,expose
from flask_login import logout_user, current_user
from flask import redirect

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN



class MyProductView(AuthenticatedAdmin):
    column_list = ['id','name','price','active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name','price']
    edit_modal = True

    def is_accessible(self):
        return current_user.is_authenticated

class MyCategory(AuthenticatedAdmin):
    column_list = ['id', 'name', 'products']


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("/admin/stats.html")


class LogoutView(BaseView):
    @expose("/")
    def index(selfs):
        logout_user()
        return redirect('/admin')


admin.add_view(MyCategory(Category,db.session))
admin.add_view(MyProductView(Product,db.session))
admin.add_view(StatsView(name='Thống kê báo cáo'))
admin.add_view(LogoutView(name='Đăng xuất'))
