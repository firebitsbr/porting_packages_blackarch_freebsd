PORTNAME=	vsvbp
DISTVERSION=	6.241a7ab
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Black box tool for Vulnerability detection in web applications.
WWW=		https://github.com/varunjammula/VSVBP

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup3@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-coverage@${PY_FLAVOR} \
		??/py-flask-babel@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-mail@${PY_FLAVOR} \
		??/py-flask-openid@${PY_FLAVOR} \
		??/py-flask-sqlalchemy@${PY_FLAVOR} \
		??/py-flask-whooshalchemy-redux@${PY_FLAVOR} \
		??/py-flask-wtf@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-flipflop@${PY_FLAVOR} \
		??/py-guess-language@${PY_FLAVOR} \
		??/py-html2text@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/py-wtforms@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
