PORTNAME=	jackdaw
DISTVERSION=	417.19e38d1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Collect all information in your domain, show you graphs on how domain objects interact with each-other and how to exploit these interactions.
WWW=		https://github.com/skelsec/jackdaw

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiosmb@${PY_FLAVOR} \
		??/py-asyauth@${PY_FLAVOR} \
		??/py-asysocks@${PY_FLAVOR} \
		??/py-bidict@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-connexion@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-flask-sqlalchemy@${PY_FLAVOR} \
		??/py-igraph@${PY_FLAVOR} \
		??/py-minikerberos@${PY_FLAVOR} \
		??/py-msldap@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pypykatz@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-swagger-ui-bundle@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-websockets@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/py-winacl@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
