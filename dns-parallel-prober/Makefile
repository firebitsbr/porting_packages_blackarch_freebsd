PORTNAME=	dns-parallel-prober
DISTVERSION=	68.422db61
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	PoC for an adaptive parallelised DNS prober.
WWW=		https://github.com/lorenzog/dns-parallel-prober

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-progressbar@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
