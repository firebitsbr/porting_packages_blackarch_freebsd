PORTNAME=	qrljacker
DISTVERSION=	222.defd5e3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	QRLJacker is a highly customizable exploitation framework to demonstrate QRLJacking Attack Vector.
WWW=		https://github.com/OWASP/QRLJacking/tree/master/QRLJacker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-jinja@${PY_FLAVOR} \
		??/py-pathlib2@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		??/py-user-agent@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
