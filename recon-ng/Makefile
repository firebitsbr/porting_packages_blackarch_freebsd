PORTNAME=	recon-ng
DISTVERSION=	v5.1.2.r7.gc08acee
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A full-featured Web Reconnaissance framework written in Python.
WWW=		https://github.com/lanmaster53/recon-ng

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dicttoxml@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-flasgger@${PY_FLAVOR} \
		??/py-flask-restful@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-jsonrpclib-pelix@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-olefile@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-pypdf2@${PY_FLAVOR} \
		??/py-rq@${PY_FLAVOR} \
		??/py-slowaes@${PY_FLAVOR} \
		??/py-unicodecsv@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
