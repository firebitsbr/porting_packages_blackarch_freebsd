PORTNAME=	vhostscan
DISTVERSION=	1.21.r68.gacc7890
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A virtual host scanner that can be used with pivot tools, detect catch-all scenarios, aliases and dynamic default pages.
WWW=		https://github.com/codingo/VHostScan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-fuzzywuzzy@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pandas@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
