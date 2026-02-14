PORTNAME=	c5scan
DISTVERSION=	30.be8845c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Vulnerability scanner and information gatherer for the Concrete5 CMS.
WWW=		https://github.com/auraltension/c5scan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
