from apps.forum.views import CategoryListView

class DashboardView(CategoryListView):
    template_name="dashboard/dashboard.html"
