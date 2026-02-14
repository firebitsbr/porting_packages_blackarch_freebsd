PORTNAME=	badministration
DISTVERSION=	16.69e4ec2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool which interfaces with management or administration applications from an offensive standpoint.
WWW=		https://github.com/ThunderGunExpress/BADministration

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-mcafee-epo@${PY_FLAVOR} \
		??/py-orionsdk@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
