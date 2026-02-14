PORTNAME=	yeti
DISTVERSION=	3427.42c9e28c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A platform meant to organize observables, indicators of compromise, TTPs, and knowledge on threats in a single, unified repository.
WWW=		https://github.com/yeti-platform/yeti

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/yarn \
		devel/git

RUN_DEPENDS=	??/libxml2 \
		??/mongodb \
		??/py-celery@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-click-plugins@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-cssselect@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-docutils@${PY_FLAVOR} \
		??/py-flask-api@${PY_FLAVOR} \
		??/py-flask-classy@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-mongoengine@${PY_FLAVOR} \
		??/py-flask-negotiation@${PY_FLAVOR} \
		??/py-flask-wtf@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-geoip2@${PY_FLAVOR} \
		??/py-html2text@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-imagesize@${PY_FLAVOR} \
		??/py-ipaddr@${PY_FLAVOR} \
		??/py-iptools@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-kombu@${PY_FLAVOR} \
		??/py-libmagic@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-maclookup@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-maxminddb@${PY_FLAVOR} \
		??/py-mongoengine@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-pdfkit@${PY_FLAVOR} \
		??/py-pdfminer@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-readability-lxml@${PY_FLAVOR} \
		??/py-redis@${PY_FLAVOR} \
		??/py-requests-file@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-snowballstemmer@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-sphinx_rtd_theme@${PY_FLAVOR} \
		??/py-sphinxcontrib-httpdomain@${PY_FLAVOR} \
		??/py-sphinxcontrib-websupport@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		??/py-url-normalize@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-urlnorm@${PY_FLAVOR} \
		??/py-vine@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/py-whois@${PY_FLAVOR} \
		??/py-wtforms@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		??/py-yara-dex@${PY_FLAVOR} \
		??/redis \
		??/wkhtmltopdf \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
