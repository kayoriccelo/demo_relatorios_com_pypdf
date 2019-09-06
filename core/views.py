import pydf
from django.http.response import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import DetailView
from rest_framework.generics import GenericAPIView
from rest_framework import filters


class BaseReportView(DetailView, GenericAPIView):
    template = 'base/report.html'
    orientation = 'portrait'
    serializer_class = None
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_class = None
    ordering = ('code', 'description')

    def get_context(self):
        return {'request': self.request.GET, 'user': self.request.user}

    def get_response(self, contexto):

        # return render(self.request, self.template, contexto)

        html = render_to_string(self.template, contexto)

        html_header_str = render_to_string('base/header.html', contexto)
        html_header_file = pydf.NamedTemporaryFile(suffix='.html')
        html_header_file.write(html_header_str.encode('utf8'))
        html_header_file.seek(0)

        html_footer_str = render_to_string('base/footer.html', contexto)
        html_footer_file = pydf.NamedTemporaryFile(suffix='.html')
        html_footer_file.write(html_footer_str.encode('utf8'))
        html_footer_file.seek(0)

        report_pdf = pydf.generate_pdf(html,
                                       page_size='A4',
                                       orientation=self.orientation,
                                       margin_left='5mm',
                                       margin_right='5mm',
                                       header_html=html_header_file.name,
                                       footer_html=html_footer_file.name,
                                       )

        response = HttpResponse(report_pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="report-example.pdf"'

        return response

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many=True)
        contexto = {'data': serializer.data,
                    'url': self.request.META['HTTP_HOST']}

        return self.get_response(contexto)
